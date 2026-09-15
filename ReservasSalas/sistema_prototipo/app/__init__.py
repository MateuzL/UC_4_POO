from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from datetime import date, timedelta, datetime
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from io import BytesIO

DAYS=['Segunda','Terça','Quarta','Quinta','Sexta']; SHIFTS=['Manhã','Tarde','Noite']
ROOMS=[{'id':1,'name':'Informática 1','category':'Informática'},{'id':2,'name':'Informática 2','category':'Informática'},{'id':3,'name':'Enfermagem 1','category':'Enfermagem'},{'id':4,'name':'Enfermagem 2','category':'Enfermagem'},{'id':5,'name':'Administração 1','category':'Administração'},{'id':6,'name':'Sala de Reuniões','category':'Reuniões'},{'id':7,'name':'Auditório','category':'Eventos'}]
TEACHERS=[{'id':1,'name':'Ana Martins','email':'ana@demo.local','password':'1234'},{'id':2,'name':'Bruno Oliveira','email':'bruno@demo.local','password':'1234'},{'id':3,'name':'Carla Souza','email':'carla@demo.local','password':'1234'}]
COURSES=[{'id':1,'name':'Técnico em Administração','short':'ADM-01','category':'Administração','shift':'Manhã','teacher_id':1},{'id':2,'name':'Técnico em Desenvolvimento de Sistemas','short':'DS-01','category':'Informática','shift':'Tarde','teacher_id':2},{'id':3,'name':'Técnico em Enfermagem','short':'ENF-01','category':'Enfermagem','shift':'Noite','teacher_id':3}]

def create_app():
 app=Flask(__name__); app.secret_key='salaflow-demo-chave'
 data={'teachers':TEACHERS.copy(),'courses':COURSES.copy(),'rooms':ROOMS.copy(),'agendas':[],'events':[{'id':1,'title':'Apresentação de projetos','date':'2026-09-25','time':'14h às 17h','location':'Auditório','type':'Apresentação','description':'Mostra dos projetos desenvolvidos pelas turmas.'},{'id':2,'title':'Reunião pedagógica','date':'2026-09-30','time':'18h às 20h','location':'Auditório','type':'Reunião','description':'Alinhamento pedagógico da equipe.'}],'notifications':[],'holidays':[]}
 today=date.today(); monday=today-timedelta(days=today.weekday()); demo=monday.strftime('%Y-%m-%d'); nxt=(monday+timedelta(days=7)).strftime('%Y-%m-%d'); app.config.update(DATA=data,DEMO_WEEK=demo,NEXT_WEEK=nxt)
 demo_rows=[]
 for day in DAYS:
  demo_rows += [(day,'Manhã',5,1,1),(day,'Tarde',1 if day in ['Segunda','Quarta','Sexta'] else 2,2,2),(day,'Noite',3 if day in ['Segunda','Quarta','Sexta'] else 4,3,3)]
 for day,shift,room,course,teacher in demo_rows: data['agendas'].append({'id':len(data['agendas'])+1,'week':demo,'day':day,'shift':shift,'room_id':room,'course_id':course,'teacher_id':teacher,'status':'Confirmada','updated_at':'Demonstração'})
 @app.context_processor
 def inject(): return {'rooms':data['rooms'],'teachers':data['teachers'],'courses':data['courses'],'days':DAYS,'shifts':SHIFTS,'data':data}
 def logged(): return 'user' in session
 def lookup(items,key,val): return next((x for x in items if x[key]==val),None)
 @app.route('/')
 def home(): return redirect(url_for('dashboard'))
 @app.route('/login',methods=['GET','POST'])
 def login():
  if request.method=='POST':
   e=request.form.get('email',''); p=request.form.get('password','')
   if e=='coordenador@demo.local' and p=='1234': session['user']={'id':0,'name':'Coordenador','role':'coordenador'}; return redirect(url_for('dashboard'))
   t=next((x for x in data['teachers'] if x['email']==e and x['password']==p),None)
   if t: session['user']={'id':t['id'],'name':t['name'],'role':'professor'}; return redirect(url_for('dashboard'))
   flash('Usuário ou senha inválidos.','error')
  return render_template('login.html')
 @app.route('/logout')
 def logout(): session.clear(); return redirect(url_for('login'))
 @app.route('/dashboard')
 def dashboard():
  if not logged(): return redirect(url_for('login'))
  week=request.args.get('week',app.config['DEMO_WEEK']); day=request.args.get('day','Todos'); shift=request.args.get('shift','Todos'); room=request.args.get('room','Todos'); teacher=request.args.get('teacher','Todos'); course=request.args.get('course','Todos')
  rows=[a for a in data['agendas'] if a['week']==week and (day=='Todos' or a['day']==day) and (shift=='Todos' or a['shift']==shift) and (room=='Todos' or str(a['room_id'])==room) and (teacher=='Todos' or str(a['teacher_id'])==teacher) and (course=='Todos' or str(a['course_id'])==course)]
  submitted={t['id']:any(a['week']==app.config['NEXT_WEEK'] and a['teacher_id']==t['id'] and a['status']=='Enviada' for a in data['agendas']) for t in data['teachers']}
  return render_template('dashboard.html',agenda=rows,week=week,events=data['events'],selected_day=day,selected_shift=shift,selected_room=room,selected_teacher=teacher,selected_course=course,submitted=submitted)
 @app.route('/agenda',methods=['GET','POST'])
 def agenda():
  if not logged(): return redirect(url_for('login'))
  if session['user']['role']!='professor': return redirect(url_for('dashboard'))
  tid=session['user']['id']; week=app.config['NEXT_WEEK']; existing=[a for a in data['agendas'] if a['week']==week and a['teacher_id']==tid]; locked=any(a['status']=='Enviada' for a in existing)
  teacher=lookup(data['teachers'],'id',tid); course=next((c for c in data['courses'] if c['teacher_id']==tid),None)
  if request.method=='POST' and not locked:
   for d in DAYS:
    for s in SHIFTS:
     val=request.form.get(f'{d}_{s}')
     old=next((a for a in existing if a['day']==d and a['shift']==s),None)
     if not val:
      if old: data['agendas'].remove(old); existing.remove(old)
      continue
     if not course or s!=course['shift']: continue
     rid=int(val); compatible=lookup(data['rooms'],'id',rid)
     if not compatible or compatible['category']!=course['category']: flash(f'Sala incompatível para {d}.','error'); return redirect(url_for('agenda'))
     conflict=next((a for a in data['agendas'] if a['week']==week and a['day']==d and a['shift']==s and a['room_id']==rid and a.get('teacher_id')!=tid),None)
     teacher_conflict=next((a for a in data['agendas'] if a['week']==week and a['day']==d and a['shift']==s and a['teacher_id']==tid and a.get('course_id')!=course['id']),None)
     if conflict or teacher_conflict: flash(f'Conflito detectado em {d} / {s}.','error'); return redirect(url_for('agenda'))
     if old: old['room_id']=rid; old['updated_at']=datetime.now().strftime('%d/%m/%Y %H:%M')
     else:
      item={'id':len(data['agendas'])+1,'week':week,'day':d,'shift':s,'room_id':rid,'course_id':course['id'],'teacher_id':tid,'status':'Em preenchimento','updated_at':datetime.now().strftime('%d/%m/%Y %H:%M')}; data['agendas'].append(item); existing.append(item)
   if request.form.get('action')=='send':
    for a in existing: a['status']='Enviada'
    flash('Agenda enviada e bloqueada.','success')
   else: flash('Rascunho salvo.','success')
   return redirect(url_for('agenda'))
  return render_template('agenda.html',week=week,existing=existing,locked=locked,teacher=teacher,course=course)
 @app.route('/coordenacao')
 def coord():
  if not logged() or session['user']['role']!='coordenador': return redirect(url_for('dashboard'))
  return render_template('coord.html',events=data['events'],holidays=data['holidays'])
 @app.route('/evento',methods=['POST'])
 def evento():
  if not logged() or session['user']['role']!='coordenador': return redirect(url_for('dashboard'))
  data['events'].append({'id':len(data['events'])+1,'title':request.form['title'],'date':request.form['date'],'time':request.form['time'],'location':'Auditório','type':request.form['type'],'description':request.form.get('description','')}); flash('Evento cadastrado no auditório.','success'); return redirect(url_for('coord'))
 @app.route('/coordenador/alterar/<int:aid>',methods=['POST'])
 def alterar(aid):
  if not logged() or session['user']['role']!='coordenador': return redirect(url_for('dashboard'))
  a=lookup(data['agendas'],'id',aid)
  if a:
   old=a.copy(); a['room_id']=int(request.form['room_id']); a['status']='Alterada pela coordenação'; a['updated_at']=datetime.now().strftime('%d/%m/%Y %H:%M'); data['notifications'].append({'teacher_id':a['teacher_id'],'message':f"Agenda alterada: {old['day']} / {old['shift']}. Sala atualizada."}); flash('Agenda alterada e professor notificado.','success')
  return redirect(url_for('dashboard',week=a['week'] if a else app.config['DEMO_WEEK']))
 @app.route('/pdf')
 def pdf():
  if not logged(): return redirect(url_for('login'))
  week=request.args.get('week',app.config['DEMO_WEEK']); day=request.args.get('day','Todos'); shift=request.args.get('shift','Todos'); room=request.args.get('room','Todos'); teacher=request.args.get('teacher','Todos'); course=request.args.get('course','Todos')
  rows=[a for a in data['agendas'] if a['week']==week and (day=='Todos' or a['day']==day) and (shift=='Todos' or a['shift']==shift) and (room=='Todos' or str(a['room_id'])==room) and (teacher=='Todos' or str(a['teacher_id'])==teacher) and (course=='Todos' or str(a['course_id'])==course)]
  buf=BytesIO(); doc=SimpleDocTemplate(buf,pagesize=landscape(A4),rightMargin=28,leftMargin=28,topMargin=28,bottomMargin=28); styles=getSampleStyleSheet(); title=ParagraphStyle('title',parent=styles['Title'],alignment=TA_CENTER,fontSize=20,spaceAfter=6); sub=ParagraphStyle('sub',parent=styles['Normal'],alignment=TA_CENTER,fontSize=10,spaceAfter=16)
  story=[Paragraph('SALAFLOW — AGENDA SEMANAL',title),Paragraph(f'Período: {week} | Filtros: Dia={day}, Turno={shift}, Sala={room}, Turma={course}, Professor={teacher} | Emitido em: {datetime.now().strftime("%d/%m/%Y %H:%M")}',sub)]
  table=[['Dia','Turno','Sala','Categoria','Turma','Professor','Status']]
  order={d:i for i,d in enumerate(DAYS)}; rows.sort(key=lambda a:(order.get(a['day'],9),SHIFTS.index(a['shift'])))
  for a in rows:
   r=lookup(data['rooms'],'id',a['room_id']); c=lookup(data['courses'],'id',a['course_id']); t=lookup(data['teachers'],'id',a['teacher_id']); table.append([a['day'],a['shift'],r['name'],r['category'],c['short']+' — '+c['name'],t['name'],a['status']])
  t=Table(table,colWidths=[55,55,90,80,210,105,105],repeatRows=1); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#153e75')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#cbd5e1')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f1f5f9')]),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); story.append(t); story.append(Spacer(1,12)); story.append(Paragraph('Observação: eventos institucionais são realizados no auditório e não ocupam as salas de aula.',styles['Normal'])); doc.build(story); buf.seek(0); resp=make_response(buf.read()); resp.headers['Content-Type']='application/pdf'; resp.headers['Content-Disposition']='inline; filename=salaflow_agenda.pdf'; return resp
 return app
