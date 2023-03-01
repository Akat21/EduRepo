<?php
$mysqli = mysqli_connect("localhost:3306", "root", "KakaPL1234", "zi2");
$res = mysqli_query($mysqli, "SELECT * from tabela");
$row = mysqli_fetch_assoc($res);
echo $row['napis'];