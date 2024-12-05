function some_function() {
alert("Yeeees!!!");
};

function setDomain () {
    var varDomain="sse.sk";
    var varMailSys="@";
    var domain=document.getElementById("idOrganization").value;
    switch(domain) {
	case "SSE":
    	varDomain="sse.sk";
	break;
	case "SSE-D":
	varDomain="sse-d.sk";
	break;
	case "SSD":
	varDomain="ssd.sk";
	break;
	case "EEM":
	varDomain="eem.sk";
	break;
	case "MEVZA":
	varDomain="mevza.sk";
	break;
    }    
    var val;
    var radios = user_frm.elements["mailsystem"];
    
    for (var i=0, len=radios.length; i<len; i++) {
        if ( radios[i].checked == true ) {
            val = radios[i].value;
            break;
        }
    }
    switch (val) {
	case "Zimbra":
	varMailSys="@" + varDomain;
	break;
	case "Kerio":
	varMailSys="@" + varDomain;
	
	break;
    }    
	varMailSys="@" + varDomain;
	//alert(val);
	document.getElementById("idMailSys").value=val;
	//alert(document.getElementById("idMailSys").value);
    	document.getElementById("idDomain").value=varMailSys;
};

function createXMLHttpRequest() {
      if (window.ActiveXObject) {
	xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
      }
      else if (window.XMLHttpRequest) {
	xmlHttp = new XMLHttpRequest();
      };
};

function send_tech_data() {
      var url = "set_tech_data";
      var params = "nazov="+document.getElementById("idMeno").value+
      "&email="+document.getElementById("idEmail").value+
      "&organization="+document.getElementById("idOrganization").value+
      "&passwd="+document.getElementById("idPasswd").value;
      var params = "uid="+document.getElementById("idMeno").value;
      createXMLHttpRequest();
//      alert(params);
      xmlHttp.onreadystatechange = doChangeState;
      xmlHttp.open("POST", url, false);
      xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xmlHttp.setRequestHeader("Content-length", params.length);
      xmlHttp.send(params);
}

function deblock_account(uid) {
      var url = "http://necm.sseintra.sk/posta/js/deblock_user.php";
      var params = "uid="+uid;
      createXMLHttpRequest();
//      alert(params);
      xmlHttp.onreadystatechange = doChangeState;
      xmlHttp.open("POST", url, false);
      xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xmlHttp.setRequestHeader("Content-length", params.length);
      xmlHttp.send(params);
      location.href = 'http://necm.sseintra.sk/posta/index.php/ECMAdmin/lock_view'
}

function deblock_sync(idRec,idDevice,loginName) {
      var url = "http://necm.sseintra.sk/posta/js/sync_approve.php";
      var params = "idrec="+idRec+"&iddevice="+idDevice+"&loginname="+loginName;
      createXMLHttpRequest();
      alert(params);
      xmlHttp.onreadystatechange = doChangeState;
      xmlHttp.open("POST", url, false);
      xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xmlHttp.setRequestHeader("Content-length", params.length);
      xmlHttp.send(params);
      location.href = 'http://necm.sseintra.sk/posta/index.php/ECMAdmin/sync_view'
}



function doChangeState() {
  if(xmlHttp.readyState == 4) {
    if(xmlHttp.status == 200) {
      alert(xmlHttp.responseText);
      document.getElementById("idUser_frm").reset();
    }
  }
}
// Ajax post
$(document).ready(function() {
$(".submit").click(function(event) {
event.preventDefault();
var user_name = $("input#name").val();
var password = $("input#pwd").val();
jQuery.ajax({
type: "POST",
url: "<?php echo base_url(); ?>" + "index.php/ajax_post_controller/user_data_submit",
dataType: 'json',
data: {name: user_name, pwd: password},
success: function(res) {
if (res)
{
// Show Entered Value
jQuery("div#result").show();
jQuery("div#value").html(res.username);
jQuery("div#value_pwd").html(res.pwd);
}
}
});
});
});
