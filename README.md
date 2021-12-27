В файлах main я сделал шаги задания с первого по седьмой
В домашнем задании я преобразовал график. Теперь он отображает работу и зарплату, на основе созданной мной базе данных.
В коде скрипта я добавил:<br>
<code>
let works = '{{ work }}';
</code><br>
<code>
const splitedLabels = works.split(" ");
</code><br>
<code>
let qs = 'dsdsd';
</code><br>
<code>
let salaries = {{ salary }};<br>
</code><br>
И тогда в описании таблицы добавляем
<code>labels: splitedLabels,</code>
и
<code>data: salaries,</code>.
Изменил функцию <b>dashboard</b>, добавив в нее соответствующие перменные:<br>
<code>
@app.route("/dashboard")
</code><br>
<code>
def dashboard():
</code><br>
<code>
return render_template('d3-dz.html',
</code><br>
<code>
cvs=get_cv(), work=get_work(), salary=get_salary(),
</code><br>
<code>
)
</code><br>
и добавил функции:<br>
<img src="./code.jpg"><br>
<b>Результат:<b><br>
<img src="./res.jpg"><br>
<img src="./res2.jpg"><br><br>
<b>Созданная база данных:<b><br>
<img src="./bd.jpg"><br>
