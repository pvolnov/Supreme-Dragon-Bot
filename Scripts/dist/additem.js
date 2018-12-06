



var f="<form class=\"add\" id=\"cart-addf\" action=\"/shop/{shopid}/add\" accept-charset=\"UTF-8\" data-remote=\"true\" method=\"post\"><input name=\"utf8\" type=\"hidden\" value=\"✓\">" +
    "<input type=\"hidden\" name=\"style\" id=\"style\" value=\"{styleid}\"><fieldset><select name=\"size\" id=\"size\"><option value=\"{sizeid}\">Yousize</option>\n" +
    "</select><a class=\"next\" href=\"/shop/tops-sweaters/ne362zj9s\">next tops/sweater &gt;</a></fieldset><fieldset id=\"add-remove-buttons\"><input type=\"submit\" name=\"commit\" value=\"add to basket\" class=\"button\">" +
    "<a class=\"button continue\" href=\"/shop\">keep shopping</a></fieldset></form>"
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
