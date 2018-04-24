from setuptools import setup, Extension

keccak_hash_module = Extension('keccak_hash',
                               sources = [
										  'mixhash/keccak/module.c',
                                          'mixhash/keccak/keccak.c',
										  'mixhash/sha3/keccak.c'							 
										  
										  ],
                               include_dirs=['mixhash/keccak','mixhash/sha3'])

qubit_hash_module = Extension('qubit_hash',
                               sources = ['mixhash/qubit/module.c',
                                          'mixhash/qubit/qubit.c',
                                          'mixhash/sha3/cubehash.c',
                                          'mixhash/sha3/echo.c',
                                          'mixhash/sha3/luffa.c',
                                          'mixhash/sha3/simd.c',
                                          'mixhash/sha3/shavite.c'
										  ],
                               include_dirs=['mixhash/qubit', 'mixhash/sha3'])



lyra2re_hash_module = Extension('lyra2re_hash',
                               sources = [
										  'mixhash/lyra2/lyra2remodule.c',
                                          'mixhash/lyra2/Lyra2RE.c',
										  'mixhash/lyra2/Sponge.c',
										  'mixhash/lyra2/Lyra2.c',
										  'mixhash/sha3/blake.c',
										  'mixhash/sha3/groestl.c',
										  'mixhash/sha3/keccak.c',
										  'mixhash/sha3/cubehash.c',
										  'mixhash/sha3/bmw.c',
										  'mixhash/sha3/skein.c'],
                               include_dirs=['mixhash/lyra2','mixhash/sha3'])

lyra2rev2_hash_module = Extension('lyra2rev2_hash',
                                sources = [
 										  'mixhash/lyra2/lyra2rev2module.c',
                                          'mixhash/lyra2/lyra2REv2.c',
 										  'mixhash/lyra2/Sponge.c',
 										  'mixhash/lyra2/Lyra2.c',
 										  'mixhash/sha3/blake.c',
 										  'mixhash/sha3/groestl.c',
 										  'mixhash/sha3/keccak.c',
 										  'mixhash/sha3/cubehash.c',
 										  'mixhash/sha3/bmw.c',
 										  'mixhash/sha3/skein.c'],
                                include_dirs=['mixhash/lyra2','mixhash/sha3'])

neoscrypt_module = Extension('neoscrypt',
                        sources = ['mixhash/neoscrypt/module.c',
                                    'mixhash/neoscrypt/neoscrypt.c'],
                        include_dirs=['mixhash/neoscrypt'])

x11_hash_module = Extension('x11_hash',
                               sources = ['mixhash/x11/module.c',
                                          'mixhash/x11/x11.c',
										  'mixhash/sha3/sph_blake.c',
										  'mixhash/sha3/sph_bmw.c',
										  'mixhash/sha3/sph_groestl.c',
										  'mixhash/sha3/sph_skein.c',
										  'mixhash/sha3/sph_jh.c',
										  'mixhash/sha3/sph_keccak.c',
										  'mixhash/sha3/sph_luffa.c',
										  'mixhash/sha3/sph_cubehash.c',
										  'mixhash/sha3/sph_shavite.c',
										  'mixhash/sha3/sph_simd.c',
										  'mixhash/sha3/sph_echo.c'],

                               include_dirs=['mixhash/x11', 'mixhash/sha3'])


setup (	name = 'mixhash',
    	version = '1.0.2',
		description = 'Make Genesis Block Proof of Work for multiple Hash Algorithms based on nasa8x.',
		long_description = 'Make Genesis Block Proof of Work for multiple Hash Algorithms on nasa8x.',
		maintainer = 'Duy Vu',
		maintainer_email = 'duyvu1311@mail.com',
		url = 'https://github.com/duyvu1311/mixhash',
		keywords = ['cryptocurrency', 'coin','bitcoin', 'dash','litecoin', 'scrypt', 'neoscrypt', 'x11', 'qubit', 'skein', 'groestl'],
		package_dir = {'mixhash': 'mixhash'},
		py_modules = ['mixhash.__init__'],
        ext_modules = [ lyra2re_hash_module, lyra2rev2_hash_module, qubit_hash_module, keccak_hash_module, neoscrypt_module, x11_hash_module])

