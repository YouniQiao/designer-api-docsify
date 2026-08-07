# createWantData

## createWantData

```TypeScript
function createWantData(want: Want): PasteData
```

构建一个Want剪贴板内容对象。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** [pasteboard.createData](arkts-basicservices-pasteboard-createdata-f.md#createdata)(mimeType:

<!--Device-pasteboard-function createWantData(want: Want): PasteData--><!--Device-pasteboard-function createWantData(want: Want): PasteData-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | 是 | Want内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | 剪贴板内容对象。 |

**示例：**

```TypeScript
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let pasteData: pasteboard.PasteData = pasteboard.createWantData(object);
```

