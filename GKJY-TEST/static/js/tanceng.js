function Show(){
        document.getElementById('shade').classList.remove('hide');
        document.getElementById('modal').classList.remove('hide');
        document.getElementById('testtip').style.visibility="hidden";
        document.getElementById('testparam').style.visibility="hidden";
    }

function Hide(){
        document.getElementById('shade').classList.add('hide');
        document.getElementById('modal').classList.add('hide');
    }

function showtip(){
        document.getElementById('testtip').style.visibility="";
    }

function showparam(){
        document.getElementById('testparam').style.visibility="";
    }


function hidetip(){
        document.getElementById('testtip').style.visibility="hidden";
    }

function hideparam(){
        document.getElementById('testparam').style.visibility="hidden";
    }
