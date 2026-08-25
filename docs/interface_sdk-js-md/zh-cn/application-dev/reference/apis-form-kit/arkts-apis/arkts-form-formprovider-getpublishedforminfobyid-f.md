# getPublishedFormInfoById

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedFormInfoById

```TypeScript
function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>
```

获取设备上当前应用程序已添加到桌面的指定卡片信息，使用Promise异步回调。

**起始版本：** 18

**废弃版本：** 20

**替代接口：** [getPublishedRunningFormInfoById](arkts-form-formprovider-getpublishedrunningforminfobyid-f.md)

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;formInfo.FormInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
