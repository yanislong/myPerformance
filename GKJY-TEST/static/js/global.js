//集成测试提交执行模块
function vailForm() {
    var obj = document.getElementsByName("iname");
    var check_val = [];
    var xhttp = new XMLHttpRequest();

    for(k in obj){
        if(obj[k].checked){
            check_val.push(obj[k].value);
        }
    }
    if (check_val == "") {
        alert("请选择要执行的模块");
        return false;
    }
    else{
        alert("已执行所选模块，等待执行结果");
    }
    xhttp.open("POST","/integrate",true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(check_val);
}

//返回列表
function fun(){
    obj = document.getElementsByName("iname");
    check_val = [];
    for(k in obj){
        if(obj[k].checked)
            check_val.push(obj[k].value);
    }
     return check_val;
}

function editInter() {
    var obj = document.getElementsByName("eid");
    var check_val = [];
    var xhttp = new XMLHttpRequest();

    for(k in obj){
        if(obj[k].checked){
            check_val.push(obj[k].value);
        }
    }
    if (check_val == "") {
        alert("请选择要执行的模块");
        return false;
    }
    else{
        alert("已执行所选模块，等待执行结果");
    }
    xhttp.open("POST","/editIntegrate",true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(check_val);
}
