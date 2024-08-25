terraform { 
  cloud { 
    
    organization = "rootedu-demoorg" 

    workspaces { 
      name = "demoworkspace" 
    } 
  } 
}
