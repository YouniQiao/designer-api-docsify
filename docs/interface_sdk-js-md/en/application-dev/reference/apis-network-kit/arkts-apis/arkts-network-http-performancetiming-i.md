# PerformanceTiming

Configures the timing for performance tracing, in ms.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## dnsTiming

```TypeScript
dnsTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the DNS resolution is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## firstReceiveTiming

```TypeScript
firstReceiveTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the first byte is received.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## firstSendTiming

```TypeScript
firstSendTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the first byte is sent.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## redirectTiming

```TypeScript
redirectTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when all redirection steps are complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## responseBodyTiming

```TypeScript
responseBodyTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the body resolution is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## responseHeaderTiming

```TypeScript
responseHeaderTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the header resolution is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## tcpTiming

```TypeScript
tcpTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the TCP connection is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## tlsTiming

```TypeScript
tlsTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the TLS connection is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## totalFinishTiming

```TypeScript
totalFinishTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the request is complete.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

## totalTiming

```TypeScript
totalTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when a callback is returned to the application.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack
