# getNfcState

## 导入模块

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## getNfcState

```TypeScript
function getNfcState(): NfcState
```

Obtains the NFC status.&lt;p&gt;The NFC status can be any of the following: &lt;ul&gt;&lt;li&gt;{@link #STATE_OFF}: Indicates that NFC is disabled. &lt;li&gt;{@link #STATE_TURNING_ON}: Indicates that NFC is being enabled.&lt;li&gt;{@link #STATE_ON}: Indicates that NFC is enabled. &lt;li&gt;{@link #STATE_TURNING_OFF}: Indicates that NFC is being disabled.&lt;/ul&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-nfcController-function getNfcState(): NfcState--><!--Device-nfcController-function getNfcState(): NfcState-End-->

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md) | Returns the NFC status. |

