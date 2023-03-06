<?php
$db = new SQLite3('mydb.db');
$db->exec("create table if not exists tab (id integer primary key autoincrement, napis text not null, liczba integer not null)");

$pdo = new PDO('sqlite:mydb.db');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_SILENT);
$pdo->exec("delete from tab");
$pdo->exec("insert into tab(napis, liczba) values('someText', 12)");

#dodanie 10 wartości
$pdo->beginTransaction();
$arr = ['jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', NULL, 'dzisiec'];
$stm1 = $pdo->prepare("insert into tab(napis,liczba) values(?,?)");
foreach($arr as $el){
    $stm1->bindValue(1,$el);
    $stm1->bindValue(2,rand(1,100));
    $stm1->execute();
}
$pdo->commit();

#dodanie null
$myvar = NULL;
$pdo->exec("insert into tab(napis, liczba) values($myvar, $myvar)");

$stm2 = $pdo->query("select * from tab");
while($row = $stm2->fetch()){
    echo $row['napis']."\n";
}
?>