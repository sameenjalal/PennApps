<html>
	<head>
		<link rel=stylesheet href="css/style.css" type="text/css">

		<script language="javascript" src="./js/jquery-1.6.4.min.js"> </script>
		<script language="javascript" src="./js/jquery.corner.js"> </script>
		<script type="text/javascript">
			function process() {
				var words = $('#searchq').val();
				$.ajax({
					type: "POST",
					url:"wordProcess.php",
					data: {data: words},
					success: function(data) {//console.log(data); return;
						dataParsed = $.parseJSON(data);
						console.log(dataParsed);

						$('#posts').html("<ul id=\"lists\" ></ul>");
						for( i in dataParsed ) {
							it = dataParsed[i];
							console.log(it);
							li="";
							if(it.type == "video" || it.type == "photo"){
								li = "<li class=\"posts_li\">" + dataParsed[i].caption + "</li>";
							}
							else if(it.type == "text" || it.type == "quote"){
								li = "<li class=\"posts_li\">" + dataParsed[i].body + "</li>";
							}
							else if(it.type == "quote"){
								li = "<li class=\"posts_li\">" + dataParsed[i].text + "</li>";
							}
							else if(it.type == "link"){
								li = "<li class=\"posts_li\">" + dataParsed[i].title + "</li>";
							}
							else if(it.type == "audio"){
								li = "<li class=\"posts_li\">" + dataParsed[i].id3_title + "</li>";
							}
							else if(it.type == "answer"){
								li = "<li class=\"posts_li\">" + dataParsed[i].answer + "</li>";
							}
							else {
								output = "No posts found!";
								li = "<li class=\"posts_li\">" + output + "</li>";
							}
							$('#lists').append(li);
							$('.posts_li').css("background-color","#FFF");
							$('.posts_li').css("padding","20px");
							$('.posts_li').css("border","20px");
							$('.posts_li').css("width","50%");
							$('.posts_li').css("margin","0 auto 20");
							$('.posts_li').css("text-align","center");
							$('.posts_li').corner();
						}
					}
				});
			}

		</script>
	</head>

	<body bgcolor="2c4762">
		<div id="search_box" class="box">
			<h1><i>Super</i> <a href="http://www.tumblr.com" target="_blank" ><img src="images/logo.png" width="15%" /></a> <i>Search</i></h1>
			<input name="searchq" size="60px" type="text" id="searchq" />
			<input type="submit" id="submitSearch" value="Search" onclick="javascript: process();" />
		</div>

		<div id="posts">
			<ul id="list"> </ul>
		</div>
	</body>
</html>
