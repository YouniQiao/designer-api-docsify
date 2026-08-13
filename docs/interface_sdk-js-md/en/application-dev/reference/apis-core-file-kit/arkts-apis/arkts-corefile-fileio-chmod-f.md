# chmod

## chmod

```TypeScript
declare function chmod(path: string, mode: number): Promise<void>
```

Changes file permissions. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-unnamed-declare function chmod(path: string, mode: number): Promise<void>--><!--Device-unnamed-declare function chmod(path: string, mode: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|).&lt;br&gt;- **0o700**: The owner has the read, write, and execute permissions.&lt;br&gt;- **0o400**: The owner has the read permission.&lt;br&gt;- **0o200**: The owner has the write permission.&lt;br&gt;- **0o100**: The owner has the execute permission.&lt;br&gt;- **0o070**: The user group has the read, write, and execute permissions.&lt;br&gt;- **0o040**: The user group has the read permission.&lt;br&gt;- **0o020**: The user group has the write permission.&lt;br&gt;- **0o010**: The user group has the execute permission.&lt;br&gt;- **0o007**: Other users have the read, write, and execute permissions.&lt;br&gt;- **0o004**: Other users have the read permission.&lt;br&gt;- **0o002**: Other users have the write permission.&lt;br&gt;- **0o001**: Other users have the execute permission. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |


## chmod

```TypeScript
declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void
```

Changes file permissions. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-unnamed-declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|).&lt;br&gt;- **0o700**: The owner has the read, write, and execute permissions.&lt;br&gt;- **0o400**: The owner has the read permission.&lt;br&gt;- **0o200**: The owner has the write permission.&lt;br&gt;- **0o100**: The owner has the execute permission.&lt;br&gt;- **0o070**: The user group has the read, write, and execute permissions.&lt;br&gt;- **0o040**: The user group has the read permission.&lt;br&gt;- **0o020**: The user group has the write permission.&lt;br&gt;- **0o010**: The user group has the execute permission.&lt;br&gt;- **0o007**: Other users have the read, write, and execute permissions.&lt;br&gt;- **0o004**: Other users have the read permission.&lt;br&gt;- **0o002**: Other users have the write permission.&lt;br&gt;- **0o001**: Other users have the execute permission. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file permissions are changed asynchronously. |

