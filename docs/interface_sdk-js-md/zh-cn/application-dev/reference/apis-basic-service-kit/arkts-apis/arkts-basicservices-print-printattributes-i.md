# PrintAttributes

定义打印参数的接口。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-print-interface PrintAttributes--><!--Device-print-interface PrintAttributes-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## colorMode

```TypeScript
colorMode?: PrintColorMode
```

表示待打印文件的色彩模式。

**类型：** [PrintColorMode](arkts-basicservices-print-printcolormode-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-colorMode?: PrintColorMode--><!--Device-PrintAttributes-colorMode?: PrintColorMode-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## copyNumber

```TypeScript
copyNumber?: int
```

表示文件打印份数。默认值为1。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-copyNumber?: int--><!--Device-PrintAttributes-copyNumber?: int-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## directionMode

```TypeScript
directionMode?: PrintDirectionMode
```

表示待打印文件的方向。

**类型：** [PrintDirectionMode](arkts-basicservices-print-printdirectionmode-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-directionMode?: PrintDirectionMode--><!--Device-PrintAttributes-directionMode?: PrintDirectionMode-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## duplexMode

```TypeScript
duplexMode?: PrintDuplexMode
```

表示待打印文件的单双面模式。

**类型：** [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-duplexMode?: PrintDuplexMode--><!--Device-PrintAttributes-duplexMode?: PrintDuplexMode-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## pageRange

```TypeScript
pageRange?: PrintPageRange
```

表示待打印文件的页面范围。

**类型：** [PrintPageRange](arkts-basicservices-print-printpagerange-i.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-pageRange?: PrintPageRange--><!--Device-PrintAttributes-pageRange?: PrintPageRange-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## pageSize

```TypeScript
pageSize?: PrintPageSize | PrintPageType
```

表示待打印文件的纸张类型。

**类型：** [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) \| PrintPageType

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-PrintAttributes-pageSize?: PrintPageSize | PrintPageType--><!--Device-PrintAttributes-pageSize?: PrintPageSize | PrintPageType-End-->

**系统能力：** SystemCapability.Print.PrintFramework

