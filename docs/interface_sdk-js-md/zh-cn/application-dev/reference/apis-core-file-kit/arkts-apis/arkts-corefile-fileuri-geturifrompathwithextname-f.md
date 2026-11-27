# getUriFromPathWithExtName

## 导入模块

```TypeScript
import { fileUri } from '@kit.CoreFileKit';
```

## getUriFromPathWithExtName

```TypeScript
function getUriFromPathWithExtName(path: string, extensionName: string): string
```

通过应用沙箱内的文件路径生成URI。路径中的中文及非数字字母的特殊字符会进行百分号编码。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-fileUri-function getUriFromPathWithExtName(path: string, extensionName: string): string--><!--Device-fileUri-function getUriFromPathWithExtName(path: string, extensionName: string): string-End-->

**系统能力：** SystemCapability.FileManagement.AppFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用沙箱内的文件路径。 |
| extensionName | string | 是 | 应用的extension ability名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回生成的URI。 |
