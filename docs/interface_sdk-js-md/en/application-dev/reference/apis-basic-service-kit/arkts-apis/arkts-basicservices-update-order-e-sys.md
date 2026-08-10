# Order (System API)

升级指令。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export enum Order--><!--Device-update-export enum Order-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## DOWNLOAD

```TypeScript
DOWNLOAD = 1
```

下载。适合仅下载升级包场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Order-DOWNLOAD = 1--><!--Device-Order-DOWNLOAD = 1-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## INSTALL

```TypeScript
INSTALL = 2
```

安装。适合直接安装已下载的升级包场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Order-INSTALL = 2--><!--Device-Order-INSTALL = 2-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## DOWNLOAD_AND_INSTALL

```TypeScript
DOWNLOAD_AND_INSTALL = 3
```

下载并安装。适合下载并安装场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Order-DOWNLOAD_AND_INSTALL = 3--><!--Device-Order-DOWNLOAD_AND_INSTALL = 3-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## APPLY

```TypeScript
APPLY = 4
```

生效。仅生效已安装的升级包，设备将重启以应用新版本，适用于已安装完成需重启生效的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Order-APPLY = 4--><!--Device-Order-APPLY = 4-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## INSTALL_AND_APPLY

```TypeScript
INSTALL_AND_APPLY = 6
```

安装并生效，执行安装后设备将重启以应用新版本。适用于需要快速完成系统更新并立即生效的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Order-INSTALL_AND_APPLY = 6--><!--Device-Order-INSTALL_AND_APPLY = 6-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

