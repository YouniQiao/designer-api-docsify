# PathPreference

```TypeScript
export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'
```

Enumerates the types of networks specified in an HTTP request. &gt; **NOTE：**&gt; &gt; It is recommended that this parameter be used in scenarios such as network concurrency. &gt; If the specified network is not activated, the system uses the default network.

**Since:** 23

<!--Device-http-export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'--><!--Device-http-export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'-End-->

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| 'auto' | Specifies the default network connection in an HTTP request. |
| 'primaryCellular' | Specifies the default cellular network connection in an HTTP request when the cellular network is activated. |
| 'secondaryCellular' | Specifies the cellular network connection of the secondary SIM card in an HTTP request when dual cellular networks are activated. |

