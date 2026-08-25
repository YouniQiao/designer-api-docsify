# setDefaultApplicationSync（系统接口）

## 导入模块

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## setDefaultApplicationSync

```TypeScript
function setDefaultApplicationSync(type: string, elementName: ElementName, userId?: number): void
```

以同步方法根据系统已定义的应用类型或者符合媒体类型格式（type/subtype）的文件类型或者 [UniformDataType](../../apis-arkdata/arkts-apis/arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)类型设置默认应用。

**起始版本：** 10

**需要权限：** ohos.permission.SET_DEFAULT_APPLICATION

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| userId | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700025](../errorcode-bundle.md#17700025-输入的type无效) |
| [17700028](../errorcode-bundle.md#17700028-输入的ability与type不匹配) |
