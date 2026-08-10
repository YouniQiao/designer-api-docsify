# DownloadConfig

下载任务的配置信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-request-interface DownloadConfig--><!--Device-request-interface DownloadConfig-End-->

**System capability:** SystemCapability.MiscServices.Download

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## background

```TypeScript
background?: boolean
```

后台任务通知开关，启用后可在通知中显示下载状态。true表示启用，false表示禁用。默认值为false。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-background?: boolean--><!--Device-DownloadConfig-background?: boolean-End-->

**System capability:** SystemCapability.MiscServices.Download

## description

```TypeScript
description?: string
```

设置下载会话的描述。默认值为空字符串。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-description?: string--><!--Device-DownloadConfig-description?: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## enableMetered

```TypeScript
enableMetered?: boolean
```

表示设置是否允许在按流量计费的连接下下载任务的配置信息。true表示允许，false表示不允许。默认值为false。

> **说明：**
> 
> Wi-Fi为非计费网络，数据流量为计费网络。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-enableMetered?: boolean--><!--Device-DownloadConfig-enableMetered?: boolean-End-->

**System capability:** SystemCapability.MiscServices.Download

## enableRoaming

```TypeScript
enableRoaming?: boolean
```

表示设置是否允许在漫游网络中下载任务的配置信息。true表示允许，false表示不允许。默认值为false。

**Type:** boolean

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-enableRoaming?: boolean--><!--Device-DownloadConfig-enableRoaming?: boolean-End-->

**System capability:** SystemCapability.MiscServices.Download

## filePath

```TypeScript
filePath?: string
```

设置下载路径。默认为调用方（即传入的context）对应的缓存路径。默认文件名从url的最后一个"/"后截取。

- FA模型下使用  
[Context.getCacheDir](../../../reference/apis-ability-kit/js-apis-inner-app-context.md#contextgetcachedir)方法获取应用存储路径。

- Stage模型下使用[Context (Stage模型的上下文基类)](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)中AbilityContext的类获取文件路径。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-filePath?: string--><!--Device-DownloadConfig-filePath?: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## header

```TypeScript
header?: Object
```

添加要包含在下载请求中的HTTPS标志头。默认值为空。

**Type:** Object

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-header?: Object--><!--Device-DownloadConfig-header?: Object-End-->

**System capability:** SystemCapability.MiscServices.Download

## networkType

```TypeScript
networkType?: int
```

设置允许下载的网络类型，通过  
[网络类型常量](../../../reference/apis-basic-services-kit/js-apis-request.md#constants)的位运算方式决定允许的网络类型，支持如下几种设置方式: 

- 仅支持蜂窝网络下载，参数为NETWORK_MOBILE或0x00000001   
- 仅支持WLAN网络下载，参数为NETWORK_WIFI或0x00010000  
- 参数默认值，支持蜂窝/WLAN网络下载，参数为NETWORK_MOBILE | NETWORK_WIFI或0x00010001。

当参数为NETWORK_MOBILE | NETWORK_WIFI时，enableMetered和enableRoaming参数不生效。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-networkType?: int--><!--Device-DownloadConfig-networkType?: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## title

```TypeScript
title?: string
```

设置下载任务名称。默认值为download。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-title?: string--><!--Device-DownloadConfig-title?: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## url

```TypeScript
url: string
```

资源地址。从API 6到API 14，最大长度为2048个字符；从API 15开始，最大长度为8192个字符。支持  
[HTTP拦截](../../../basic-services/request/app-file-upload-download.md#http拦截)功能。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-DownloadConfig-url: string--><!--Device-DownloadConfig-url: string-End-->

**System capability:** SystemCapability.MiscServices.Download

