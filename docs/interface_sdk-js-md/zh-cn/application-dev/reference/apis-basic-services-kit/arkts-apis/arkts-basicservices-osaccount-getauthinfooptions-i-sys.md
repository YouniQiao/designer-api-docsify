# GetAuthInfoOptions（系统接口）

表示[查询认证凭据信息](arkts-basicservices-osaccount-useridentitymanager-c-sys.md#getauthinfo)的可选参数集合。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## accountId

```TypeScript
accountId?: int
```

系统账号标识，默认为undefined。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## authType

```TypeScript
authType?: AuthType
```

认证类型，默认为undefined。

**类型：** AuthType

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。
