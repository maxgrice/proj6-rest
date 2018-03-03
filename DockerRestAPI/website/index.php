<html>
    <head>
        <title>Brevet Times</title>
    </head>

    <body>
        <h1>Brevet Time Listings</h1>
        <ul>
            <?php
            $all = file_get_contents('http://laptop-service/listAll');
            echo "   All Times:\n"
            foreach ($all as $time) {
	            echo "<li>$time</li>"
	        }
	        
	        $all_json = file_get_contents('http://laptop-service/listAll/json');
	        echo "   All Times (JSON):\n"
            foreach ($all_json as $time) {
	            echo "<li>$time</li>"
	        }
	 
	        $all_csv = file_get_contents('http://laptop-service/listAll/csv');
	        echo "   All Times (CSV):\n"
            foreach ($all_csv as $time) {
	            echo "<li>$time</li>"
	        }
	        
	        $open_json = file_get_contents('http://laptop-service/listOpenOnly/json');
	        echo "   Open Times (JSON):\n"
            foreach ($open_json as $time) {
	            echo "<li>$time</li>"
	        }
	  
	        $close_json = file_get_contents('http://laptop-service/listCloseOnly/json');
	        echo "   Close Times (JSON):\n"
            foreach ($close_json as $time) {
	            echo "<li>$time</li>"
	        }
	
	        $open_csv = file_get_contents('http://laptop-service/listOpenOnly/csv');
	        echo "   Open Times (CSV):\n"
            foreach ($open_csv as $time) {
	            echo "<li>$time</li>"
	        }
	  
	        $close_csv = file_get_contents('http://laptop-service/listCloseOnly/csv');
	        echo "   Close Times (CSV):\n"
            foreach ($open_csv as $time) {
	            echo "<li>$time</li>"
	        }
	
            ?>
        </ul>
    </body>
</html>
