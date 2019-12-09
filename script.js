var addr = "192.168.1.100"
var port = "8000"

function makeQuery(name, age){
    jQuery.get("http://"+addr+":"+port+"/dataQuery/"+ name+ "/" + age, function(result){
        myRes = jQuery.parseJSON(result);
        toStore= "<table border='2' bordercolor='#397056'><tr><td><strong>name</strong></td><td><strong>age</strong></td></tr>";
        $.each(myRes, function(i, element){
            toStore= toStore+ "<tr><td>"+element.name+"</td><td>" + element.age+ "</td></td></tr>";
        })
        toStore= toStore+ "</table>"
        $('#theDataDiv').text('');
        $('<br/>').appendTo('#theDataDiv');
        $(toStore).appendTo('#theDataDiv');
        $('<br/>').appendTo('#theDataDiv');
    })
}
