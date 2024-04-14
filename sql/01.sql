CREATE TABLE IF NOT EXISTS
  user (
    user_cd_user TEXT not null PRIMARY KEY,
    user_nm_name TEXT not null,
    user_tx_username TEXT not null,
    user_tx_password TEXT not null,
    user_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    user_df_updated_at TIMESTAMP not null default CURRENT_TIMESTAMP
  );

CREATE TABLE IF NOT EXISTS
  list (
    list_cd_list TEXT not null PRIMARY KEY,
    list_nm_name TEXT not null,
    list_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    list_df_updated_at TIMESTAMP not null default CURRENT_TIMESTAMP
  );

CREATE TABLE IF NOT EXISTS
  list_user (
    lius_cd_list_user TEXT not null PRIMARY KEY,
    lius_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    user_cd_user TEXT not null,
    list_cd_list TEXT not null,
    FOREIGN KEY (user_cd_user) REFERENCES user (user_cd_user) ON DELETE CASCADE,
    FOREIGN KEY (list_cd_list) REFERENCES list (list_cd_list) ON DELETE CASCADE
  );

CREATE TABLE IF NOT EXISTS
  section (
    sect_cd_section TEXT not null PRIMARY KEY,
    sect_nm_name TEXT not null,
    sect_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    sect_df_updated_at TIMESTAMP not null default CURRENT_TIMESTAMP
  );
  
CREATE TABLE IF NOT EXISTS
  product (
    prod_cd_product TEXT not null PRIMARY KEY,
    prod_nm_name TEXT not null,
    prod_vl_price REAL not null,
    prod_tx_image_url TEXT,
    prod_cd_barcode TEXT,
    prod_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    prod_df_updated_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    sect_cd_section TEXT not null,
    FOREIGN KEY (sect_cd_section) REFERENCES section (sect_cd_section)
  );

CREATE TABLE IF NOT EXISTS
  list_product (
    lipr_cd_list_product TEXT not null PRIMARY KEY,
    lipr_nr_quantity INTEGER not null,
    lipr_df_created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    lipr_df_updated_at TIMESTAMP not null default CURRENT_TIMESTAMP,
    list_cd_list TEXT not null,
    prod_cd_product TEXT not null,
    FOREIGN KEY (list_cd_list) REFERENCES list (list_cd_list) ON DELETE CASCADE,
    FOREIGN KEY (prod_cd_product) REFERENCES product (prod_cd_product) ON DELETE CASCADE
  );