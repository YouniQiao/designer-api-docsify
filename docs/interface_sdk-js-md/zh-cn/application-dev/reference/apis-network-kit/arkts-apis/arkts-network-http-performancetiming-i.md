# PerformanceTiming

Counting the time taken of various stages of HTTP request.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-http-export interface PerformanceTiming--><!--Device-http-export interface PerformanceTiming-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## dnsTiming

```TypeScript
dnsTiming: double
```

Time taken from startup to DNS resolution completion, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-dnsTiming: double--><!--Device-PerformanceTiming-dnsTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## firstReceiveTiming

```TypeScript
firstReceiveTiming: double
```

Time taken from startup to receiving the first byte, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-firstReceiveTiming: double--><!--Device-PerformanceTiming-firstReceiveTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## firstSendTiming

```TypeScript
firstSendTiming: double
```

Time taken from startup to start sending the first byte, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-firstSendTiming: double--><!--Device-PerformanceTiming-firstSendTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## redirectTiming

```TypeScript
redirectTiming: double
```

Time taken from startup to completion of all redirection steps, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-redirectTiming: double--><!--Device-PerformanceTiming-redirectTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## responseBodyTiming

```TypeScript
responseBodyTiming: double
```

Time taken from HTTP Request to body completion, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-responseBodyTiming: double--><!--Device-PerformanceTiming-responseBodyTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## responseHeaderTiming

```TypeScript
responseHeaderTiming: double
```

Time taken from HTTP request to header completion, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-responseHeaderTiming: double--><!--Device-PerformanceTiming-responseHeaderTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## tcpTiming

```TypeScript
tcpTiming: double
```

Time taken from startup to TCP connection completion, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-tcpTiming: double--><!--Device-PerformanceTiming-tcpTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## tlsTiming

```TypeScript
tlsTiming: double
```

Time taken from startup to TLS connection completion, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-tlsTiming: double--><!--Device-PerformanceTiming-tlsTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## totalFinishTiming

```TypeScript
totalFinishTiming: double
```

Time taken from startup to the completion of the request, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-totalFinishTiming: double--><!--Device-PerformanceTiming-totalFinishTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

## totalTiming

```TypeScript
totalTiming: double
```

Time taken from HTTP Request to callback to the application, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PerformanceTiming-totalTiming: double--><!--Device-PerformanceTiming-totalTiming: double-End-->

**系统能力：** SystemCapability.Communication.NetStack

