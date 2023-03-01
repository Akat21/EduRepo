<?php
$db = new SQLite3('mydb.db');

$db->exec("create table if not exists tabela (liczba int, napis text)");
$db->exec("insert into tabela values(11, 'aaaa')");

$res = $db->query("select * from tabela");
while($row = $res->fetchArray()){
    echo $row['napis'] . "\n";    
}