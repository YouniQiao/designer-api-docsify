# PerformanceInfo

预下载的性能信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cacheDownload-interface PerformanceInfo--><!--Device-cacheDownload-interface PerformanceInfo-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## connectTime

```TypeScript
readonly connectTime: double
```

从启动到tcp连接完成所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly connectTime: double--><!--Device-PerformanceInfo-readonly connectTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## dnsTime

```TypeScript
readonly dnsTime: double
```

从启动到dns解析完成所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly dnsTime: double--><!--Device-PerformanceInfo-readonly dnsTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## firstReceiveTime

```TypeScript
readonly firstReceiveTime: double
```

从启动到接收第一个字节所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly firstReceiveTime: double--><!--Device-PerformanceInfo-readonly firstReceiveTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## firstSendTime

```TypeScript
readonly firstSendTime: double
```

从启动到开始发送第一个字节所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly firstSendTime: double--><!--Device-PerformanceInfo-readonly firstSendTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## redirectTime

```TypeScript
readonly redirectTime: double
```

从启动到完成所有重定向步骤所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly redirectTime: double--><!--Device-PerformanceInfo-readonly redirectTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## tlsTime

```TypeScript
readonly tlsTime: double
```

从启动到tls连接完成所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly tlsTime: double--><!--Device-PerformanceInfo-readonly tlsTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## totalTime

```TypeScript
readonly totalTime: double
```

从启动到完成请求所需的时间，单位：毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PerformanceInfo-readonly totalTime: double--><!--Device-PerformanceInfo-readonly totalTime: double-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

