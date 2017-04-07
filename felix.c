/*comandes AT felix*/

"AT+CSQ"    //comprova cobertura
"AT+CGATT?" //comprova AtachedPackedDomainService

//processant
portSim.println("AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"");
portSim.print(F("AT+SAPBR=3,1,\"APN\",\""));
portSim.print(F("AT+SAPBR=3,1,\"USER\",\""));
portSim.print(F("AT+SAPBR=3,1,\"PWD\",\""));
portSim.println(F("AT+SAPBR=1,1")); 
portSim.println(F("AT+SAPBR=2,1"));
portSim.println(F("AT+SAPBR=2,1"));
portSim.print(F("AT+HTTPPARA=\"URL\",\"things.ubidots.com/api/v1.6/variables/"));
portSim.print(id);
portSim.print(F("/values?token="));
portSim.print(_token);
portSim.println("\"");
portSim.println(F("AT+HTTPPARA=\"CONTENT\",\"application/json\""));
portSim.print(F("AT+HTTPDATA="));
portSim.print(strlen(data));
portSim.print(F(","));
portSim.println(120000);
portSim.println(F("AT+HTTPACTION=1"));  // HTTPACTION=1 is a POST method
portSim.println(F("AT+HTTPREAD"));
portSim.println(F("AT+HTTPINIT"));
portSim.println(F("AT+HTTPPARA=\"CID\",1"));
portSim.print(F("AT+HTTPPARA=\"UA\","));
portSim.print(USER_AGENT);
portSim.println(F("\""));
portSim.println(F("AT+HTTPTERM"));
