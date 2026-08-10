# getMifareUltralight

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getMifareUltralight

```TypeScript
function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag
```

Obtains an {@link MifareUltralightTag} object based on the tag information.During tag reading, if the tag supports the MIFARE Ultralight technology,an {@link MifareUltralightTag} object will be created based on the tag information.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag--><!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | 是 | Indicates the dispatched tag information. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md) | The { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

