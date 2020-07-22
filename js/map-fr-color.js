jQuery(document).ready(function(){
    var map = new jvm.Map({
        container: jQuery("#map-fr"),
        map: 'fr_merc',
        regionsSelectable: true
    });

    $.getJSON("python/data.json")
    .done(function(data) {
        var color = "";
        $.each(data.departments,function(){
            switch(this.color){
                case 1:
                    color = "blue";
                    break;
                case 2:
                    color = "green";
                    break;
                case 3:
                    color = "red";
                    break;
                case 4:
                    color = "yellow";
                    break;
                default:
                    color="";
                    break;
            };
            if(this.code.length == 4)
                $("path[data-code='FR-0"+this.code.charAt(3)+"']").css("fill",color);
            else
                $("path[data-code='"+this.code+"']").css("fill",color);
        });
    });
});
