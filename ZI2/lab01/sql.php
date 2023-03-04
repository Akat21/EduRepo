<?php
$db = new mysqli("localhost:3306", "root", "KakaPL1234", "zi2");

$db->query("create table if not exists tabela (liczba int, napis text)");
$db->query("insert into tabela values(11, 'aaaa')");

$res = $db->query("select * from tabela");
while($row = $res->fetch_array()){
    echo $row['napis'] . "\n";    
}