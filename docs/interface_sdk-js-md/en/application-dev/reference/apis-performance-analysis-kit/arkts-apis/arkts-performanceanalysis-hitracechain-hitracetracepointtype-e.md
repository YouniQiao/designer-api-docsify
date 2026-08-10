# HiTraceTracepointType

跟踪埋点类型枚举。用于标识业务流程中的关键节点，例如CS和CR用于标记客户端请求的发送和接收，SS和SR用于标记服务端请求的接收和发送，GENERAL用于标记无法归入上述四种场景的其他关键节点。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hiTraceChain-enum HiTraceTracepointType--><!--Device-hiTraceChain-enum HiTraceTracepointType-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## CS

```TypeScript
CS = 0
```

客户端发送(Client Send)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HiTraceTracepointType-CS = 0--><!--Device-HiTraceTracepointType-CS = 0-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## CR

```TypeScript
CR = 1
```

客户端接收(Client Receive)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HiTraceTracepointType-CR = 1--><!--Device-HiTraceTracepointType-CR = 1-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## SS

```TypeScript
SS = 2
```

服务端发送(Server Send)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HiTraceTracepointType-SS = 2--><!--Device-HiTraceTracepointType-SS = 2-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## SR

```TypeScript
SR = 3
```

服务端接收(Server Receive)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HiTraceTracepointType-SR = 3--><!--Device-HiTraceTracepointType-SR = 3-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## GENERAL

```TypeScript
GENERAL = 4
```

通用类型，标识CS、CR、SS、SR四种场景之外的埋点。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HiTraceTracepointType-GENERAL = 4--><!--Device-HiTraceTracepointType-GENERAL = 4-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

