# PerformanceTiming

性能打点(单位：ms)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from '@kit.NetworkKit';
```

## dnsTiming

```TypeScript
dnsTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到DNS解析完成耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## firstReceiveTiming

```TypeScript
firstReceiveTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到接收第一个字节的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## firstSendTiming

```TypeScript
firstSendTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到开始发送第一个字节的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## redirectTiming

```TypeScript
redirectTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到完成所有重定向步骤的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## responseBodyTiming

```TypeScript
responseBodyTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到body解析完成的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## responseHeaderTiming

```TypeScript
responseHeaderTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到header解析完成的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## tcpTiming

```TypeScript
tcpTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到TCP连接完成耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## tlsTiming

```TypeScript
tlsTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到TLS连接完成耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## totalFinishTiming

```TypeScript
totalFinishTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求到完成请求的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## totalTiming

```TypeScript
totalTiming: double
```

从[request](arkts-network-http-httprequest-i.md#request)请求回调到应用程序的耗时。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack
