



var f="<form class=\"add\" id=\"cart-addf\" action=\"/shop/{}/add\" accept-charset=\"UTF-8\" data-remote=\"true\" method=\"post\">\n" +
    "    <input name=\"utf8\" type=\"hidden\" value=\"✓\"><input type=\"hidden\" name=\"style\" id=\"style\" value=\"{}\">\n" +
    "    <fieldset><select name=\"size\" id=\"size\">\n" +
    "        <option value=\"{}\">MySize</option>\n" +
    "    </select></fieldset>\n" +
    "    <fieldset id=\"add-remove-buttons\"><input type=\"submit\" name=\"commit\" value=\"add to cart\" class=\"button\"><a\n" +
    "            class=\"button continue\" href=\"/shop\">keep shopping</a></fieldset>\n" +
    "</form>";
document.getElementsByTagName("header")[0].innerHTML=f;

$("#cart-addf").submit();

// var f="<form class=\"add\" id=\"cart-addf\" action=\"/shop/303892/add\" accept-charset=\"UTF-8\" data-remote=\"true\" method=\"post\">\n" +
//     "    <input name=\"utf8\" type=\"hidden\" value=\"вњ“\"><input type=\"hidden\" name=\"style\" id=\"style\" value=\"24657\">\n" +
//     "    <fieldset><select name=\"size\" id=\"size\">\n" +
//     "        <option value=\"52227\">MySize</option>\n" +
//     "    </select></fieldset>\n" +
//     "    <fieldset id=\"add-remove-buttons\"><input type=\"submit\" name=\"commit\" value=\"add to cart\" class=\"button\"><a\n" +
//     "            class=\"button continue\" href=\"/shop\">keep shopping</a></fieldset>\n" +
//     "</form>";
// document.getElementsByTagName("header")[0].innerHTML=f;
//
// $("#cart-addf").submit();
