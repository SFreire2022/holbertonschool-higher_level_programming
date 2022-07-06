-- Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
<<<<<<< HEAD
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
=======
MODIFY name VARCHAR(256)
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,;
>>>>>>> df34248d17a3b3aa5ce3e061220c97c344cc5c17
