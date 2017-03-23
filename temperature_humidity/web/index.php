<?php
require_once(dirname(__FILE__) . "/BusinessLogicLayer/tempHumClass.php");

$tempHum = new tempHumClass();
$tempHumResult = $tempHum->getAllTempData();
$currentT = $tempHumResult[0]->temp;
$currentH = $tempHumResult[0]->hum;
$tempHumResult = array_reverse($tempHumResult);
?>
<html>
    <head>
        <meta http-equiv="refresh" content="15" >
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load('current', {'packages': ['corechart']});
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var Tdata = google.visualization.arrayToDataTable([
                    ['Date', 'Temperature'],
<?php
foreach ($tempHumResult as $tempHumI) {
    echo '[\'' . $tempHumI->date . '\',  ' . $tempHumI->temp . '],';
}
?>
                ]);

                var Hdata = google.visualization.arrayToDataTable([
                    ['ID', 'Humidity'],
<?php
foreach ($tempHumResult as $tempHumI) {
    echo '[\'' . $tempHumI->id . '\',  ' . $tempHumI->hum . '],';
}
?>
                ]);

                var Toptions = {
                    title: 'Last 12 Hrs Room Temp',
                    curveType: 'function',
                    legend: {position: 'bottom'}
                };

                var Hoptions = {
                    title: 'Last 12 Hrs Room Humidity',
                    curveType: 'function',
                    legend: {position: 'bottom'}
                };

                var Tchart = new google.visualization.LineChart(document.getElementById('T_chart'));
                var Hchart = new google.visualization.LineChart(document.getElementById('H_chart'));

                Tchart.draw(Tdata, Toptions);
                Hchart.draw(Hdata, Hoptions);
            }
        </script>
    </head>
    <body>
        <div style="float: left">
            <div id="T_chart" style="width: 900px; height: 500px"></div>
            <div id="H_chart" style="width: 900px; height: 500px"></div>
        </div>


        <div style="float: left; border-right: black; border-right-style: double">
            <div>
                <h3 style="color: green">Last Read Room Temperature:</h3>
            </div>
            <div>
                <h1 style="color: green">" <?php echo $currentT; ?> &#8451; "</h1>
            </div>
        </div>
        <div style="float: left">
            <div>
                <h3 style="color: green">Last Read Room Humidity:</h3>
            </div>
            <div>
                <h1 style="color: green">" <?php echo $currentH; ?> "</h1>
            </div>
        </div>
    </body>
</html>
