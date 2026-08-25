# PathPreference

```TypeScript
export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'
```

Enumerates the types of networks specified in an HTTP request.

> **NOTE：**&gt;
> It is recommended that this parameter be used in scenarios such as network concurrency.

> If the specified network is not activated, the system uses the default network.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**System capability:** SystemCapability.Communication.NetStack

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| 'auto' |
| 'primaryCellular' |
| 'secondaryCellular' |
