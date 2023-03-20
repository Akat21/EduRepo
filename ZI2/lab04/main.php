<?php
    require_once __DIR__.'/vendor/autoload.php';

    use \Doctrine\DBAL\DriverManager;
    use \Doctrine\DBAL\Schema\Schema;

    $connection_params = array(
        'dbname' => 'zi2',
        'user' => 'root',
        'password' => 'KakaPL1234',
        'host' => 'localhost:3306',
        'driver' => 'pdo_mysql',
    );
    
    $conn = DriverManager::getConnection($connection_params);

    #PIERWSZY PODPUNKT
    $queryBuilder = $conn->createQueryBuilder();
    $queryBuilder->select('customerName', 'creditLimit')
        ->from('customers')
        ->where('country = "USA"')
        ->orderBy('creditLimit','DESC');
    $stmt = $queryBuilder->executeQuery();
    $results = $stmt->fetchAllAssociative();

    foreach($results as $row){
        echo $row['customerName'] . ' ' . $row['creditLimit'] . PHP_EOL;
    }

    #DRUGI PODPUNKT
    $queryBuilder = $conn->createQueryBuilder();
    $queryBuilder->select('c.customerNumber', 'c.customerName', 'e.firstName', 'e.lastName')
        ->from('customers', 'c')
        ->join('c','employees', 'e','c.salesRepEmployeeNumber = e.employeeNumber');
    $stmt = $queryBuilder->executeQuery();
    $results = $stmt->fetchAllAssociative();

    foreach($results as $row){
        echo $row['customerNumber'] . ' ' . $row['customerName'] . ' ' . $row['firstName'] . ' ' . $row['lastName'] . PHP_EOL;
    }

    $mytable = 'my_table';
    $schema = new Schema();
    $tab =$schema->createTable($mytable);
    $tab->addColumn('id', 'integer', ['unsigned'=>true, 'autoincrement'=>true]);
    $tab->addColumn('napis', 'string');
    $tab->addColumn('liczba', 'integer');
    $tab->setPrimaryKey(['id']);

    $sql = $schema->toSql($conn->getDatabasePlatform());

    $conn->executeStatement($sql[0]);

    $queryBuilder->insert('my_table')
        ->values([
            'liczba' => '?',
            'napis' => '?'
        ])
        ->setParameters([13, 'XD']);

    $queryBuilder->executeStatement();
?>