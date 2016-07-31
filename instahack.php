<?php


$username=$_POST['username'];

function getInstaID($username)
{

    $username = strtolower($username);
    $token = "1931492888.1677ed0.8f098298b22a4ad3ae82709dfcb712c0";
    $url = "https://api.instagram.com/v1/users/search?q=".$username."&access_token=".$token;
    $get = file_get_contents($url);
    $json = json_decode($get);

    foreach($json->data as $user)
    {
        if($user->username == $username)
        {
            return $user->id;
        }
    }

    return '00000000'; 
}



?>

<form method="POST" ACTION="instahack.php">
<input type="text" name="username" />

<input type="submit"/>
<div><?php echo getInstaID($username)?></div>
</form>


