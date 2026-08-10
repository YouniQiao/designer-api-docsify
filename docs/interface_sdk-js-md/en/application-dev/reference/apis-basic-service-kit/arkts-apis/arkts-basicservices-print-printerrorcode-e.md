# PrintErrorCode

打印错误代码的枚举。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-print-enum PrintErrorCode--><!--Device-print-enum PrintErrorCode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_NONE

```TypeScript
E_PRINT_NONE = 0
```

表示没有错误。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_NONE = 0--><!--Device-PrintErrorCode-E_PRINT_NONE = 0-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_NO_PERMISSION

```TypeScript
E_PRINT_NO_PERMISSION = 201
```

表示没有许可。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_NO_PERMISSION = 201--><!--Device-PrintErrorCode-E_PRINT_NO_PERMISSION = 201-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_INVALID_PARAMETER

```TypeScript
E_PRINT_INVALID_PARAMETER = 401
```

表示无效的参数。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_INVALID_PARAMETER = 401--><!--Device-PrintErrorCode-E_PRINT_INVALID_PARAMETER = 401-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_GENERIC_FAILURE

```TypeScript
E_PRINT_GENERIC_FAILURE = 13100001
```

表示一般打印失败。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_GENERIC_FAILURE = 13100001--><!--Device-PrintErrorCode-E_PRINT_GENERIC_FAILURE = 13100001-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_RPC_FAILURE

```TypeScript
E_PRINT_RPC_FAILURE = 13100002
```

表示RPC失败。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_RPC_FAILURE = 13100002--><!--Device-PrintErrorCode-E_PRINT_RPC_FAILURE = 13100002-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_SERVER_FAILURE

```TypeScript
E_PRINT_SERVER_FAILURE = 13100003
```

表示打印服务失败。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_SERVER_FAILURE = 13100003--><!--Device-PrintErrorCode-E_PRINT_SERVER_FAILURE = 13100003-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_INVALID_EXTENSION

```TypeScript
E_PRINT_INVALID_EXTENSION = 13100004
```

表示打印扩展无效。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_INVALID_EXTENSION = 13100004--><!--Device-PrintErrorCode-E_PRINT_INVALID_EXTENSION = 13100004-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_INVALID_PRINTER

```TypeScript
E_PRINT_INVALID_PRINTER = 13100005
```

表示打印机无效。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_INVALID_PRINTER = 13100005--><!--Device-PrintErrorCode-E_PRINT_INVALID_PRINTER = 13100005-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_INVALID_PRINT_JOB

```TypeScript
E_PRINT_INVALID_PRINT_JOB = 13100006
```

表示打印任务无效。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_INVALID_PRINT_JOB = 13100006--><!--Device-PrintErrorCode-E_PRINT_INVALID_PRINT_JOB = 13100006-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_FILE_IO

```TypeScript
E_PRINT_FILE_IO = 13100007
```

表示文件输入/输出错误。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_FILE_IO = 13100007--><!--Device-PrintErrorCode-E_PRINT_FILE_IO = 13100007-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_TOO_MANY_FILES

```TypeScript
E_PRINT_TOO_MANY_FILES = 13100010
```

表示文件数量超过上限，当前上限99个。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrintErrorCode-E_PRINT_TOO_MANY_FILES = 13100010--><!--Device-PrintErrorCode-E_PRINT_TOO_MANY_FILES = 13100010-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_SMB_LOGIN_LOCKOUT

```TypeScript
E_PRINT_SMB_LOGIN_LOCKOUT = 13100012
```

表示当前SMB协议共享打印机账号因多次登录失败而被锁定。

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintErrorCode-E_PRINT_SMB_LOGIN_LOCKOUT = 13100012--><!--Device-PrintErrorCode-E_PRINT_SMB_LOGIN_LOCKOUT = 13100012-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_SMB_CONNECTION_FAILURE

```TypeScript
E_PRINT_SMB_CONNECTION_FAILURE = 13100013
```

表示SMB协议共享打印机连接失败（发生网络错误、主机不可达或端口被阻止）。

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintErrorCode-E_PRINT_SMB_CONNECTION_FAILURE = 13100013--><!--Device-PrintErrorCode-E_PRINT_SMB_CONNECTION_FAILURE = 13100013-End-->

**System capability:** SystemCapability.Print.PrintFramework

## E_PRINT_SMB_INVALID_CREDENTIALS

```TypeScript
E_PRINT_SMB_INVALID_CREDENTIALS = 13100014
```

表示SMB协议共享打印机账号/密码错误。

**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintErrorCode-E_PRINT_SMB_INVALID_CREDENTIALS = 13100014--><!--Device-PrintErrorCode-E_PRINT_SMB_INVALID_CREDENTIALS = 13100014-End-->

**System capability:** SystemCapability.Print.PrintFramework

