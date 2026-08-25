# IInputer（系统接口）

凭据输入器回调。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## onGetData

```TypeScript
onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void
```

通知调用者获取数据的回调函数。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authSubType | [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md) | 是 |
| callback | [IInputData](arkts-basicservices-osaccount-iinputdata-i-sys.md) | 是 |
| options | [GetInputDataOptions](arkts-basicservices-osaccount-getinputdataoptions-i-sys.md) | 是 |
