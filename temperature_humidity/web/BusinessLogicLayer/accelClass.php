<?php


require_once(dirname(__FILE__) . "/../DataAccessLayer/DA_QueryClass.php");

class accelClass {
    public function getAllAccelData() {
        $qc = new QueryClass();
        return json_decode($qc->selectQueryRun('SELECT * FROM `accel_data`'));
    }
}
