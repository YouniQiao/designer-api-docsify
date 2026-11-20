# HuksPQCSigMode

```TypeScript
export enum HuksPQCSigMode
```

后量子密码（PQC）算法签名模式枚举。

**起始版本：** 26.1.0

<!--Device-huks-export enum HuksPQCSigMode--><!--Device-huks-export enum HuksPQCSigMode-End-->

**系统能力：** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_EXTERNAL_MU

```TypeScript
HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2
```

外部 Mu 模式（External Mu）：输入为预先计算好的 64 字节消息代表值 Mu。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2-End-->

**系统能力：** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_PREHASH

```TypeScript
HUKS_PQC_SIG_MODE_PREHASH = 1
```

预哈希模式（Pre-hash）：先对消息进行哈希，再对哈希值签名。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PREHASH = 1--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PREHASH = 1-End-->

**系统能力：** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_PURE

```TypeScript
HUKS_PQC_SIG_MODE_PURE = 0
```

纯模式（Pure）：直接对原始消息签名，无需预先哈希。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PURE = 0--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PURE = 0-End-->

**系统能力：** SystemCapability.Security.Huks.Core
