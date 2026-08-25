# createAVMusicTemplate

## 导入模块

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## createAVMusicTemplate

```TypeScript
function createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate
```

创建音频模板，返回音频模板实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [accessType](../../apis-telephony-kit/arkts-apis/arkts-telephony-esim-accessrule-i-sys.md) | [AVMusicTemplateType](arkts-avsession-avmusictemplate-avmusictemplatetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AVMusicTemplate](arkts-avsession-avmusictemplate-avmusictemplate-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [35000001](../errorcode-avmusictemplate.md#35000001-音频模板创建失败) |
