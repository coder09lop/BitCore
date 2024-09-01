#load the opencore engine
engine = OpenCoreEngine()
#load the opencore config
config = OpenCoreConfig()
#load the opencore boot arguments
boot_args = OpenCoreBootArgs()
#load the opencore boot arguments
boot_args.load()
#the opencore boot arguments
boot_args.parse()
#apply the opencore boot arguments
boot_args.apply()
#load the opencore boot arguments
boot_args.load()