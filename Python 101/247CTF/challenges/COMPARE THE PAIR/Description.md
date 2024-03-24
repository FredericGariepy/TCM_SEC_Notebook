### COMPARE THE PAIR
##### RATED MODERATE
Can you identify a way to bypass our login logic? MD5 is supposed to be a one-way function right?
___
Going to the challenge url we get greeded with:
```php
<?php
  require_once('flag.php');
  $password_hash = "0e902564435691274142490923013038";
  $salt = "f789bbc328a3d1a3";
  if(isset($_GET['password']) && md5($salt . $_GET['password']) == $password_hash){
    echo $flag;
  }
  echo highlight_file(__FILE__, true);
?>
```
