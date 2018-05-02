
<!DOCTYPE html>
<html>
<head>
<title>jBox Demos</title>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0">

<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/jBox.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/plugins/Notice/jBox.Notice.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/plugins/Confirm/jBox.Confirm.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/plugins/Image/jBox.Image.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/NoticeFancy.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipBorder.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipBorderThick.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipDark.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipSmall.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipSmallGray.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Source/themes/TooltipError.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Demo.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Demo/Playground/Playground.Avatars.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/Demo/Playground/Playground.Login.css">

<%@ page contentType="text/html;charset=UTF-8" %>
<script src="https://code.jquery.com/jquery-3.2.1.js"></script>

<header>
<nav class="container">
<a href="https://stephanwagner.me/jBox/documentation">Documentation</a>
<a href="https://stephanwagner.me/jBox/demos">More Demos</a>
<a href="https://stephanwagner.me/Coding" id="stephan"><span>Stephan Wagner</span></a>
</nav>
</header>

<main class="container">

<h2>현재 기분</h2>
<div class="targets-wrapper">
<div id="Tooltip-1" class="target">Hover me</div>
<div id="Tooltip-2" class="target">Hover me</div>
<div id="Tooltip-3" class="target">Hover me</div>
<div id="Tooltip-4" class="target">Hover me</div>
<div id="Tooltip-5" class="target">Hover me</div>
<div id="Tooltip-6" class="target">Hover me</div>
<div id="Tooltip-7" class="target-click">Click me</div>
<div id="Tooltip-8" class="target-click">Click me</div>
</div>

<h2>음식</h2>

<div class="targets-wrapper">
<div id="Modal-1" class="target-click">Click me</div>
<div id="Modal-2" class="target-click">Click me</div>
<div id="Modal-3" class="target-click">Click me</div>
<div class="target-click" data-confirm onclick="new jBox('Notice', {content: 'Yay! You clicked the confirm button', color: 'green', attributes: {y: 'bottom'}})">Click me</div>
</div>

<h2>같이보는 사람</h2>
<div class="targets-wrapper">
<div id="Notice-1" class="target-notice">Click me</div>
<div id="Notice-2" class="target-notice">Click me</div>
<div id="Notice-3" class="target-notice">Click me</div>
<div id="Notice-4" class="target-notice">Click me</div>
<div id="Notice-5" class="target-notice">Click me</div>
<div id="Notice-6" class="target-notice">Click me</div>
<div id="Notice-7" class="target-notice">Click me</div>
<div id="Notice-8" class="target-notice">Click me</div>
</div>

<h2>분위기 선택</h2>
<div class="targets-wrapper">
<a class="demo-img" href="https://stephanwagner.me/img/jBox/demo/image1.jpg" data-jbox-image="gallery1" title="Navigate with your keyboard: Press the [right] or [left] key"><img src="https://stephanwagner.me/img/jBox/demo/image1-preview.jpg" alt=""></a>
<a class="demo-img" href="https://stephanwagner.me/img/jBox/demo/image2.jpg" data-jbox-image="gallery1" title="jBox is smart, the next image gets preloaded"><img src="https://stephanwagner.me/img/jBox/demo/image2-preview.jpg" alt=""></a>
<a class="demo-img" href="https://stephanwagner.me/img/jBox/demo/image3.jpg" data-jbox-image="gallery1" title="You can easily group your images into galleries"><img src="https://stephanwagner.me/img/jBox/demo/image3-preview.jpg" alt=""></a>
<a class="demo-img" href="https://stephanwagner.me/img/jBox/demo/image4.jpg" data-jbox-image="gallery1" title="As usual, attaching jBox to images is easy as pie"><img src="https://stephanwagner.me/img/jBox/demo/image4-preview.jpg" alt=""></a>
<a href="https://stephanwagner.me/img/jBox/demo/NOT-FOUND.jpg" data-jbox-image="gallery1" title="You can adjust this image-not-found notice with CSS"></a>
</div>

<h2>Playground</h2>

<div class="targets-wrapper">
<div id="DemoAvatars" class="target-click">Click me</div>
<div id="DemoLogin" class="target-click">Click me</div>
</div>

</main>

<script src="${pageContext.request.contextPath}/resources/Source/jBox.js"></script>
<script src="${pageContext.request.contextPath}/resources/Source/plugins/Notice/jBox.Notice.js"></script>
<script src="${pageContext.request.contextPath}/resources/Source/plugins/Confirm/jBox.Confirm.js"></script>
<script src="${pageContext.request.contextPath}/resources/Source/plugins/Image/jBox.Image.js"></script>
<script src="${pageContext.request.contextPath}/resources/Demo/Demo.js"></script>
<script src="${pageContext.request.contextPath}/resources/Demo/Playground/Playground.Avatars.js"></script>
<script src="${pageContext.request.contextPath}/resources/Demo/Playground/Playground.Login.js"></script>

</body>
</html>