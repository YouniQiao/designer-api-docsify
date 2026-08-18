# PerformanceTiming

Configures the timing for performance tracing, in ms.

**Since:** 23

<!--Device-http-export interface PerformanceTiming--><!--Device-http-export interface PerformanceTiming-End-->

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

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-dnsTiming: double--><!--Device-PerformanceTiming-dnsTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## firstReceiveTiming

```TypeScript
firstReceiveTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the first byte is received.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-firstReceiveTiming: double--><!--Device-PerformanceTiming-firstReceiveTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## firstSendTiming

```TypeScript
firstSendTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the first byte is sent.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-firstSendTiming: double--><!--Device-PerformanceTiming-firstSendTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## redirectTiming

```TypeScript
redirectTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when all redirection steps are complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-redirectTiming: double--><!--Device-PerformanceTiming-redirectTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## responseBodyTiming

```TypeScript
responseBodyTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the body resolution is complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-responseBodyTiming: double--><!--Device-PerformanceTiming-responseBodyTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## responseHeaderTiming

```TypeScript
responseHeaderTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the header resolution is complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-responseHeaderTiming: double--><!--Device-PerformanceTiming-responseHeaderTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## tcpTiming

```TypeScript
tcpTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the TCP connection is complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-tcpTiming: double--><!--Device-PerformanceTiming-tcpTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## tlsTiming

```TypeScript
tlsTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the TLS connection is complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-tlsTiming: double--><!--Device-PerformanceTiming-tlsTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## totalFinishTiming

```TypeScript
totalFinishTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when the request is complete.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-totalFinishTiming: double--><!--Device-PerformanceTiming-totalFinishTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

## totalTiming

```TypeScript
totalTiming: double
```

Duration from the time when the [request](arkts-network-http-httprequest-i.md#request) is sent to the time when a callback is returned to the application.

**Type:** double

**Since:** 23

<!--Device-PerformanceTiming-totalTiming: double--><!--Device-PerformanceTiming-totalTiming: double-End-->

**System capability:** SystemCapability.Communication.NetStack

