# Faults

定义任务失败的原因。

> **说明：**
> 
> API version 12及以下版本，只支持串行的尝试连接域名相关ip，且不支持单个ip的连接时间控制，如果DNS返回的首个ip是阻塞的，可能会导致握手超时，进而引发TIMEOUT错误。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-agent-enum Faults--><!--Device-agent-enum Faults-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## OTHERS

```TypeScript
OTHERS = 0xFF
```

表示其他故障。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Faults-OTHERS = 0xFF--><!--Device-Faults-OTHERS = 0xFF-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## DISCONNECTED

```TypeScript
DISCONNECTED = 0x00
```

表示网络断开连接。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Faults-DISCONNECTED = 0x00--><!--Device-Faults-DISCONNECTED = 0x00-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## TIMEOUT

```TypeScript
TIMEOUT = 0x10
```

表示任务超时。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Faults-TIMEOUT = 0x10--><!--Device-Faults-TIMEOUT = 0x10-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## PROTOCOL

```TypeScript
PROTOCOL = 0x20
```

表示协议错误，例如：服务器内部错误（500）、无法处理的数据区间（416）等。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Faults-PROTOCOL = 0x20--><!--Device-Faults-PROTOCOL = 0x20-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## PARAM

```TypeScript
PARAM = 0x30
```

表示参数错误，例如：url格式错误等。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Faults-PARAM = 0x30--><!--Device-Faults-PARAM = 0x30-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## FSIO

```TypeScript
FSIO = 0x40
```

表示文件系统io错误，例如：打开/查找/读取/写入/关闭。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Faults-FSIO = 0x40--><!--Device-Faults-FSIO = 0x40-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## DNS

```TypeScript
DNS = 0x50
```

表示DNS解析错误。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Faults-DNS = 0x50--><!--Device-Faults-DNS = 0x50-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## TCP

```TypeScript
TCP = 0x60
```

表示TCP连接错误。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Faults-TCP = 0x60--><!--Device-Faults-TCP = 0x60-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## SSL

```TypeScript
SSL = 0x70
```

表示SSL连接错误，例如：证书错误、证书校验失败错误等。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Faults-SSL = 0x70--><!--Device-Faults-SSL = 0x70-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## REDIRECT

```TypeScript
REDIRECT = 0x80
```

表示重定向错误。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Faults-REDIRECT = 0x80--><!--Device-Faults-REDIRECT = 0x80-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## LOW_SPEED

```TypeScript
LOW_SPEED = 0x90
```

表示任务速度过低。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Faults-LOW_SPEED = 0x90--><!--Device-Faults-LOW_SPEED = 0x90-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

