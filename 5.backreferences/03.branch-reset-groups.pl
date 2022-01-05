$Regex_Pattern = '^[0-9]{2}(\-{3}?|\-?|\.?|\:?)[0-9]{2}\1[0-9]{2}\1[0-9]{2}$';

$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}