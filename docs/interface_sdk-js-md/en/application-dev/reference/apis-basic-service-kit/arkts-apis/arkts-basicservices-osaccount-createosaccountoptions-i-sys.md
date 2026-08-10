# CreateOsAccountOptions (System API)

表示用于创建系统账号的可选参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-osAccount-interface CreateOsAccountOptions--><!--Device-osAccount-interface CreateOsAccountOptions-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## allowedPreinstalledBundles

```TypeScript
allowedPreinstalledBundles?: Array<string>
```

表示预置应用允许名单，仅名单中的应用可以被安装在设备上，默认为std::nullopt。

**Type:** Array&lt;string&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-CreateOsAccountOptions-allowedPreinstalledBundles?: Array<string>--><!--Device-CreateOsAccountOptions-allowedPreinstalledBundles?: Array<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## disallowedPreinstalledBundles

```TypeScript
disallowedPreinstalledBundles?: Array<string>
```

表示预置应用禁止名单，名单中的应用不可被安装在设备上，默认为空列表。

**Type:** Array&lt;string&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-CreateOsAccountOptions-disallowedPreinstalledBundles?: Array<string>--><!--Device-CreateOsAccountOptions-disallowedPreinstalledBundles?: Array<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## shortName

```TypeScript
shortName: string
```

表示账号短名称（用作个人文件夹目录）。 

**约束：** 

1. 不允许出现的字符：&lt; &gt; | : " * ? / \2. 不允许独立出现的字符串：.或..3. 长度不超过255个字符。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-CreateOsAccountOptions-shortName: string--><!--Device-CreateOsAccountOptions-shortName: string-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## token

```TypeScript
token?: Uint8Array
```

表示从认证管理接口获取的token，默认为空。

**Type:** Uint8Array

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-CreateOsAccountOptions-token?: Uint8Array--><!--Device-CreateOsAccountOptions-token?: Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

