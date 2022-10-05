// 根据用户输入判断是否正确
window.onload = function () {
    var oInp = document.getElementById('http');
    var bu = document.getElementById('bu');
    oInp.onmouseout=function(){
        aa = oInp.value;
        if(aa.startsWith("http")){
            bu.disabled = false;   
        }else{
            if (aa !== ''){
                alert('请输入http开头的API');
            }
            bu.disabled = true;
        }

    }
}